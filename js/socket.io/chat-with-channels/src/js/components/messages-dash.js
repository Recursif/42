
import React, { Component } from 'react'


class MessagesDash extends Component {
    constructor(props) {
        super(props)
    }
    
    render() {
        return this.props.messages.success ? (
            <div role="alert" className="alert alert-success m-3">
                {this.props.messages.success.map((message, index) => <div key={index}>{message.msg}</div>)}
            </div>
        ) : this.props.messages.error ? (
            <div role="alert" className="alert alert-danger m-3">
                {this.props.messages.error.map((message, index) => <div key={index}>{message.msg}</div>)}
            </div>
        ) : this.props.messages.info ? (
            <div role="alert" className="alert alert-info m-3">
                {this.props.messages.info.map((message, index) => <div key={index}>{message.msg}</div>)}
            </div>
        ) : null
    }
}

export default MessagesDash