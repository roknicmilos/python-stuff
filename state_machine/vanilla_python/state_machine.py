from enum import Enum
from typing import Dict, Callable


class State(Enum):
    """Possible states of the application"""
    IDLE = "idle"
    STARTING = "starting"
    CONNECTED = "connected"
    RECORDING = "recording"
    SAVING = "saving"
    ERROR = "error"


class Event(Enum):
    """Events that can trigger state transitions"""
    CAMERA_CONNECTED = "camera_connected"
    PRESSURE_SENSOR_CONNECTED = "pressure_sensor_connected"
    CAMERA_DISCONNECTED = "camera_disconnected"
    PRESSURE_SENSOR_DISCONNECTED = "pressure_sensor_disconnected"
    START_RECORDING = "start_recording"
    STOP_RECORDING = "stop_recording"
    SAVE_DATA = "save_data"
    SAVE_COMPLETE = "save_complete"
    ERROR_OCCURRED = "error_occurred"


class StateMachine:
    """
    A simple state machine that manages application state based on
    device inputs and events.
    """

    def __init__(self):
        self.current_state = State.IDLE
        self.camera_connected = False
        self.pressure_sensor_connected = False

        # Define valid state transitions: {(current_state, event): next_state}
        self.transitions: Dict[tuple, State] = {
            # From IDLE
            (State.IDLE, Event.CAMERA_CONNECTED): State.STARTING,
            (State.IDLE, Event.PRESSURE_SENSOR_CONNECTED): State.STARTING,

            # From STARTING
            (State.STARTING, Event.CAMERA_CONNECTED): State.CONNECTED,
            (State.STARTING, Event.PRESSURE_SENSOR_CONNECTED): State.CONNECTED,

            # From CONNECTED
            (State.CONNECTED, Event.START_RECORDING): State.RECORDING,
            (State.CONNECTED, Event.CAMERA_DISCONNECTED): State.IDLE,
            (State.CONNECTED, Event.PRESSURE_SENSOR_DISCONNECTED): State.IDLE,

            # From RECORDING
            (State.RECORDING, Event.STOP_RECORDING): State.CONNECTED,
            (State.RECORDING, Event.SAVE_DATA): State.SAVING,
            (State.RECORDING, Event.ERROR_OCCURRED): State.ERROR,

            # From SAVING
            (State.SAVING, Event.SAVE_COMPLETE): State.CONNECTED,
            (State.SAVING, Event.ERROR_OCCURRED): State.ERROR,

            # From ERROR
            (State.ERROR, Event.CAMERA_DISCONNECTED): State.IDLE,
            (State.ERROR, Event.PRESSURE_SENSOR_DISCONNECTED): State.IDLE,
        }

        # Optional: callbacks for state entry
        self.state_callbacks: Dict[State, Callable] = {
            State.CONNECTED: self._on_connected,
            State.RECORDING: self._on_recording,
            State.ERROR: self._on_error,
        }

    def handle_event(self, event: Event) -> bool:
        """
        Process an event and transition to a new state if valid.
        Returns True if transition occurred, False otherwise.
        """
        # Update device connection tracking
        if event == Event.CAMERA_CONNECTED:
            self.camera_connected = True
        elif event == Event.CAMERA_DISCONNECTED:
            self.camera_connected = False
        elif event == Event.PRESSURE_SENSOR_CONNECTED:
            self.pressure_sensor_connected = True
        elif event == Event.PRESSURE_SENSOR_DISCONNECTED:
            self.pressure_sensor_connected = False

        # Check if transition is valid
        transition_key = (self.current_state, event)

        if transition_key in self.transitions:
            # Special logic: only transition to CONNECTED if both devices are connected
            next_state = self.transitions[transition_key]
            if next_state == State.CONNECTED:
                if not (self.camera_connected and self.pressure_sensor_connected):
                    print(
                        f"Cannot transition to CONNECTED: both devices must be connected")
                    return False

            old_state = self.current_state
            self.current_state = next_state

            print(
                f"State transition: {old_state.value} -> {self.current_state.value} (event: {event.value})")

            # Execute callback if exists
            if self.current_state in self.state_callbacks:
                self.state_callbacks[self.current_state]()

            return True
        else:
            print(
                f"Invalid transition: {self.current_state.value} cannot handle {event.value}")
            return False

    def get_state(self) -> State:
        """Get current state"""
        return self.current_state

    # State entry callbacks (examples)
    def _on_connected(self):
        print("  → Both devices connected and ready")

    def _on_recording(self):
        print("  → Recording started")

    def _on_error(self):
        print("  → Error state entered - requires intervention")


# Demo usage
if __name__ == "__main__":
    sm = StateMachine()

    print(f"Initial state: {sm.get_state().value}\n")

    # Simulate device connection sequence
    print("=== Connecting Devices ===")
    sm.handle_event(Event.CAMERA_CONNECTED)
    sm.handle_event(Event.PRESSURE_SENSOR_CONNECTED)

    print("\n=== Starting Recording ===")
    sm.handle_event(Event.START_RECORDING)

    print("\n=== Saving Data ===")
    sm.handle_event(Event.SAVE_DATA)
    sm.handle_event(Event.SAVE_COMPLETE)

    print("\n=== Invalid Transition Test ===")
    sm.handle_event(Event.SAVE_DATA)  # Can't save when not recording

    print("\n=== Error Scenario ===")
    sm.handle_event(Event.START_RECORDING)
    sm.handle_event(Event.ERROR_OCCURRED)

    print(f"\nFinal state: {sm.get_state().value}")
