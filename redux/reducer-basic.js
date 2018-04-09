/* Reducers specify how the application's
state changes in response to actions sent to the store.
Remember that actions only describe the fact that something happened, but don't
describe how the application's state changes

Designing the State Shape

In Redux, all the application state is stored as a single object.
It's a good to think of its shape before writing any code.

Try to keep the data separate from the UI state.
*/

{
  visibilityFilter: 'SHOW_ALL',
  todos: [
  {
    text: 'Consider using Redux'
    completed: true,
  }, {
    text: 'Keep all the state in a single tree',
    completed: false
  }
  ]
}

/*
Handling actions

(previousState, action) => newState
*/

import { VisibilityFilters } from './actions'

const initialState = {
  visibilityFilter: VisibilityFilters.SHOW_ALL,
  todos: []
}

function todoApp(state, action) {
  if (typeof state === 'undefined') {
    return initialState
  }
  // For now, don't handle any actions
  // and just return the state given to us
  return state
}
