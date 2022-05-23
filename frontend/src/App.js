import React, { Component } from 'react';
import TommMain from "./components/TommMain.js";
import PageIntro from "./components/PageIntro.js"
import PageResult from "./components/PageResult.js"
import PageUpload from "./components/PageUpload.js"
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      scroll_y: 0,
      screen_y: 0
    };
  }

  render() {
    window.addEventListener('scroll', (e) => {
      let window_scroll = window.scrollY;
      let screen_height = window.screen.height;
      this.setState({
        scroll_y: window_scroll,
        screen_y : screen_height
      });
    });

    return (
      <div className="App">
        <TommMain></TommMain>
        <PageIntro scroll_y={this.state.scroll_y} screen_y={this.state.screen_y}></PageIntro>
        <PageResult></PageResult>
        <PageUpload></PageUpload>
      </div>
    );
  }
}

export default App;
