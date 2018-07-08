
const channels = (state = [], action) => {
    switch (action.type) {
        case 'ADD_FETCHED_CHANNELS':
            return action.events
        case 'ADD_CHANNEL':
            return [
                action.event,
                ...state
            ]
        case 'UPDATE_CHANNEL':
            var eventsList = state.slice()
            const event = eventsList.find((event) => event._id == action.event._id)
            const eventIndex = eventsList.indexOf(event)
            
            if (eventIndex == -1) {
                return state
            } else {
                eventsList[eventIndex] = action.event
                return eventsList
            }
        case 'TOGGLE_CHANNEL':
            return state.map(event =>
                (event._id === action.id)
                    ? {...event, finish: !event.finish}
                    : event
            )
        default:
            return state
    }
}
  
export default events