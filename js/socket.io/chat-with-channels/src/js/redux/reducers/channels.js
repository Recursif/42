
const channels = (state = [], action) => {
    switch (action.type) {
        case 'ADD_FETCHED_CHANNELS':
            return action.channels
        case 'ADD_CHANNEL':
            return [
                action.channel,
                ...state
            ]
        case 'UPDATE_CHANNEL':
            var channelsList = state.slice()
            const channel = channelsList.find((channel) => channel._id == action.channel._id)
            const channelIndex = channelsList.indexOf(channel)
            
            if (channelIndex == -1) {
                return state
            } else {
                channelsList[channelIndex] = action.channel
                return channelsList
            }
        default:
            return state
    }
}
  
export default channels