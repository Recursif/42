import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import Web3 from 'web3';
import './style.css';

var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));

class Block extends Component {
  constructor(props) {
    super(props);
    this.state = {
      block: []
    }
  }

  componentWillMount() {
    var block_hash = this.props.match.params.blockHash;
    this.getBlockState(block_hash);
  }

  componentWillReceiveProps(nextProps) {
    var block_hash_old = this.props.match.params.blockHash;
    var block_hash_new = nextProps.match.params.blockHash;

    if (block_hash_old !== block_hash_new)
    this.getBlockState(block_hash_new);
  }

  getBlockState(block_hash) {
    console.log("Block hash: " + block_hash);

    const getPromise = async (block_hash) => {
      var currBlockObj = await web3.eth.getBlock(block_hash);
      console.log(JSON.stringify(currBlockObj));

      this.setState({
        block_id: currBlockObj.nuimber,
        block_hash: currBlockObj.hash,
        block_ts: Date(parseInt(this.state.block.timestamp, 10)).toString(),
        block_txs: parseInt(currBlockObj.transactions.slice().length, 10),
        block: currBlockObj
      })
    }
    getPromise(block_hash);
  }

  render() {

    const block = this.state.block;
    const difficulty = parseInt(block.difficulty, 10);
    const difficultyTotal = parseInt(block.totalDifficulty, 10)


    return (
      <div className="Block">
        <h2>Block Info</h2>
        <div>
          <table>
            <tbody>
              <tr><td className="tdLabel">Height: </td><td>{this.state.block.number}</td></tr>
              <tr><td className="tdLabel">Timestamp: </td><td>{this.state.block_ts}</td></tr>
              <tr><td className="tdLabel">Transactions: </td><td>{this.state.block_txs}</td></tr>
              <tr><td className="tdLabel">Hash: </td><td>{this.state.hash}</td></tr>
              <tr><td className="tdLabel">Parent hash: </td>
              <td><Link to={`../block/${this.state.block.parentHash}`}>{this.state.block.parentHash}</Link></td></tr>
              <tr><td className="tdLabel">Nonce: </td><td>{this.state.block.nonce}</td></tr>
              <tr><td className="tdLabel">Size: </td><td>{this.state.block.size} bytes</td></tr>
              <tr><td className="tdLabel">Difficulty: </td><td>{difficulty}</td></tr>
              <tr><td className="tdLabel">Difficulty: </td><td>{difficultyTotal}</td></tr>
              <tr><td className="tdLabel">Gas limit: </td><td>{block.gasLimit}</td></tr>
              <tr><td className="tdLabel">Sha3Uncles: </td><td>{block.sha3Uncles}</td></tr>
              <tr><td className="tdLabel">Extra data: </td><td>{this.state.block.extraData}</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    );
  }
}

export default Block;
