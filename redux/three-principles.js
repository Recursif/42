/*
Single source of truth

the state of your whole application is stored in an object tree within
a single store.
*/


console.log(store.getState())

/* Prints
{
  visibilityFilter: 'SHOW_ALL',
  todos: [
    {
      text: 'Consider using redux'
      completed: true,
    },
    {
      text: 'Keep all state in a single tree',
      completed: false
    }
  ]
}
*/

/*
State is read-only

the only way to change state is to emit an action,
an object describing what happened.
*/

store.dispatch ({
  type: 'COMPLETE_TODO',
  index: 1
})

store.dispatch ({
  type: 'SET_VISIBILITY_FILTER',
  filter: 'SHOW_COMPLETED'
})

/*
Changes are made with pure functions

To specify how the state tree is transformed by actions,
you write pure reducers.

Reducers are just pure functions that take the previous state and an action, and return the next state.
*/

function visibility(state = 'SHOW_ALL', action) {
  switch (action.type) {
    case 'SET_VISIBILITY_FILTER':
      return action.filter
    default:
      return state
  }
}

function todos(state = [], action) {
  switch (action.type) {
    case 'ADD_TODO':
      return [
        ...state,
        {
          text: action.text,
          completeted: false
        }
      ]
    case 'COMPLETE_TODO':
      return state.map((todo, index) => {
        if (index === action.index) {
          return Object.assign({}, todo, {
            completed: true
          })
        }
        return todo
      })
    default:
      return state
  }
}

import { combineReducers, createStore } from 'redux'
const reducer = combineReducers({ visibilityFilter, todos })
const store = createStore(reducer)
