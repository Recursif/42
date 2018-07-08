
import React, { Component } from 'react'
import { Layout, Menu, Breadcrumb, List } from 'antd';

const { Header, Content, Footer } = Layout;

//import fetchChannels from '../../redux/action/channels'


class Home extends Component {
    constructor(props) {
        super(props)
    }
    render() {
        return (
            <div>
                <Content style={{ "padding": "50px 50px", "maxWidth": "600px", "margin": "auto" }}>
                    <List
                        span={4}
                        size="large"
                        header={<div style={{ "textAlign": "center" }}>Channels</div>}
                        footer={<div style={{ "textAlign": "center" }}>Add a channels</div>}
                        bordered
                        dataSource={this.props.channels}
                        renderItem={item => (<List.Item>{item.name}</List.Item>)}
                    />
                </Content>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return state
}

export default Home