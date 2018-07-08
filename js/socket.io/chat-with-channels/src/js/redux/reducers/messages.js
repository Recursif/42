
const messages = (state = {}, action) => {
    switch (action.type) {
        case 'FAILURE':
            return {
                error: action.messages
            }
        case 'SUCCESS':
            return {
                success: action.messages
            }
        case 'INFO':
            return {
                info: action.messages
            }
        case 'CLEAR_MESSAGES':
            return {}
        default:
            return state
    }
}
  
export default messages
  