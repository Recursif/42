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


function todos(state = [], action) {
  switch (action.type) {
    case ADD_TODO:
      return [
        ...state,
        {
          text: action.text,
          completed: false
        }
      ]
    case TOGGLE_TODO:
      return state.map((todo, index) => {
        if (index === action.index) {
          return Object.assign({}, todo, {
            completed: !todo.completed
          })
        }
        return todo
      })
    default:
      return state
  }
}

function visibilityFilter(state = SHOW_ALL, action) {
  switch (action.type) {
    case SET_VISIBILITY_FILTER:
        return action.filter
    default:
      return state
  }
}

function todoApp(state = {}, action) {
  return {
    visibilityFilter: visibilityFilter(state.visibilityFilter, action),
    todos: todos(state.todos, action)
  }
}
/* Note that each of these reducers is managing its own part of the global
The state parameter is different for every reducer, and corresponds to the
part of the state it manages.
*/

/*Redux provides a utility called combinedReducers() that does the same
boilerplate logic that the todoApp above currently does. */


import { combineReducers } from 'redux';

const todoApp = combineReducers({
  visibilityFilter,
  todos
})

export default todoApp



/*We create a copy of the state with Oject.assign()
Object.assign(state, { visibilityFilter: action.filter })

*/
