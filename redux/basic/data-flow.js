Redux architecture resolves around a strict undirectional data flow

This means that all data in an app follows the same lifecycle pattern
making the logic of your app more predictable and easier to understand.
It aslo encourages data normalization, so that you don t end up with multiple,
independent copies of the same data that are unaware of the another.

The data lifecylcle in any Redux app follows these 4 steps:

1. You call store.dispatch(action)

An action is a plain object describing what happened. For example:

{ type: 'LIKE_ARTICLE', articleId: 42}
{ type: 'FETCH_USER_SUCESS', response: { id: 3, name: 'Mary'}}
{ type: 'ADD_TODO', text: 'read the redux docs.' }

2. The redux store calls the reducer function you gave it.

the store wil pass two argument to the reducer: the current state tree and the action.
For example, in the todo app, the root reducer might receive something like:

// The current app state

let previousState = {
  visibleTodoFilter: 'SHOW_ALL',
  todos: [
    {
      text: 'Read the docs.',
      complete: false
    }
  ]
}

// The action being performed (adding a todo)

let action = {
  type: 'ADD_TODO',
  text: 'Understand the flow.'
}

// Your reducer returns the next application state
let nextState = todoApp(previousState, action)

3. The root reducer may combine the output of the multiple reducers into a single state tree

How you structure the root reducer is completely up to you.
Redux ships with a combineReducers() helper function,
useful for “splitting” the root reducer into separate functions
that each manage one branch of the state tree.

function todos(state = [], action) {
  // Somehow calculate it...
  return nextState
}
 
function visibleTodoFilter(state = 'SHOW_ALL', action) {
  // Somehow calculate it...
  return nextState
}
 
let todoApp = combineReducers({
  todos,
  visibleTodoFilter
})

When you emit an action, todoApp returned by combineReducers call both reducers:
let nextTodos = todos(state.todos, action)
let nextVisibleTodoFilter = visibleTodoFilter(state.visibleTodoFilter, action)


It will then combine both sets of results into a single state tree:

 return {
   todos: nextTodos,
   visibleTodoFilter: nextVisibleTodoFilter
 }


4. The redux store saves the complete state tree returned by the root reducer.

This new tree is now the next state of your app!
Every listener registered with store.subscribe(listener) will now be invoked; listeners may call store.getState() to get the current state.

Now, the UI can be updated to reflect the new state. If you use bindings like React Redux, this is the point at which component.setState(newState) is called.
