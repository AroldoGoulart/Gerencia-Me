import React from 'react';
import axios from 'axios';
import data from "./data/alunos.json"; 

export default class PersonList extends React.Component {
  constructor(props) {
    super(props);
    this.state = { id: 0 };
  }

  componentDidMount() {
    axios.get(`http://127.0.0.1:5000/json/alunos`)
      .then(res => {
        const persons = res.data;
      })
  }

  change(event) {
    this.setState({ id: event.target.value });
    axios.get(`http://127.0.0.1:5000/delete`, {params: {Id: this.state.id}})
      .then(res => {
        const persons = res.data;
      })
  }

  render() {
    return (
      <div>
      <input value={this.state.id} onChange={(e) => this.change(e)} />
      <p>Hello {this.state.name}!</p>
       <ul>
      {<p>{JSON.stringify(data)}</p>}
      </ul>
      </div>

     
    )
  }
}