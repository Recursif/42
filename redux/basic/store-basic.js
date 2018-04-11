
Action = what happened

Reducers = update the state according to those actions

The store is the object that brings the actions and the reducers together:
- Holds the application state;
- Allows access to state via getState();
- Allows state to be updated via dispatch(action);
- Registers listners via subscribe(listener);
- Handles unregistering of listners via the function returned by subscribe(listener);

import { createStore } from 'redux'
import todoApp from './reducers'
const store = createStore(todoApp, windows.STATE_FROM_SERVER)

//Dispatching actions

import {
  addTodo,
  toggleTodo,
  setVisibilityFilter,
  VisibilityFilters
} from './actions'

// Log the initial State

console.log(store.getState())

// Every time the state changes, log it
// Note that subscribe() returns a function for unregistering the listener

const unsubcribe = store.subscribe(() =>
  console.log(store.getState())
)
 
// Dispatch some actions
store.dispatch(addTodo('Learn about actions'))
store.dispatch(addTodo('Learn about reducers'))
store.dispatch(addTodo('Learn about store'))
store.dispatch(toggleTodo(0))
store.dispatch(toggleTodo(1))
store.dispatch(setVisibilityFilter(VisibilityFilters.SHOW_COMPLETED))
 
// Stop listening to state updates
unsubscribe()
