import unittest
from unittest.mock import MagicMock
from EventEmitter import EventEmitter

class TestEventEmitter(unittest.TestCase):
    def test_should_initialise_emitter(self):
        # arrange
        emitter = EventEmitter()

        # act
        is_initialised = emitter.events is not None

        # assert
        self.assertTrue(is_initialised, 'EventEmitter has not been initialised')

    def test_should_add_listener(self):
        # arrange
        event_name = 'test'
        emitter = EventEmitter()
        listener = MagicMock(return_value=True)

        # act
        emitter.on(event_name, listener)
        is_listener_in_events = listener in emitter.events[event_name]

        # assert
        self.assertTrue(is_listener_in_events, 'Event has not been registered in listeners')

    def test_should_run_listener_on_emit(self):
        # arrange
        event_name = 'test'
        emitter = EventEmitter()
        listener = MagicMock(return_value=True)

        # act
        emitter.on(event_name, listener)
        emitter.emit(event_name)

        # assert
        listener.assert_called_once_with()

    def test_should_run_listener_on_emit_with_args(self):
        # arrange
        event_name = 'test'
        emitter = EventEmitter()
        expected_arguments = {'test': ['some specific list']}
        listener = MagicMock(return_value=True)

        # act
        emitter.on(event_name, listener)
        emitter.emit(event_name, expected_arguments)

        # assert
        listener.assert_called_once_with(expected_arguments)

    def test_should_run_all_listener_on_emit(self):
        # arrange
        event_name = 'test'
        emitter = EventEmitter()
        listener = MagicMock(return_value=True)
        second_listener = MagicMock(return_value=True)

        # act
        emitter.on(event_name, listener)
        emitter.on(event_name, second_listener)
        emitter.emit(event_name)

        # assert
        listener.assert_called_once_with()
        second_listener.assert_called_once_with()

    def test_should_not_run_listener_on_other_emit(self):
        # arrange
        event_name = 'test'
        event_to_emit = 'test2'
        emitter = EventEmitter()
        listener = MagicMock(return_value=True)

        # act
        emitter.on(event_name, listener)
        emitter.emit(event_to_emit)

        # assert
        listener.assert_not_called()

    def test_should_remove_listener(self):
        # arrange
        event_name = 'test'
        emitter = EventEmitter()
        listener = MagicMock(return_value=True)
        emitter.on(event_name, listener)
        is_listener_registered = listener in emitter.events[event_name]
        self.assertTrue(is_listener_registered, 'Listener was not registered')

        # act
        emitter.remove_listener(event_name,listener)
        is_listener_registered = listener in emitter.events[event_name]

        # assert
        self.assertFalse(is_listener_registered, 'Listener was not removed')

if __name__ == '__main__':
    unittest.main()
