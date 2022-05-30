import React, { Component } from 'react';
import TommMain from "./components/TommMain.js";
import PageIntro from "./components/PageIntro.js"
import PageResult from "./components/PageResult.js"
import PageUpload from "./components/PageUpload.js"
import PageFooter from "./components/PageFooter.js"
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      scroll_y: 0,
      screen_y: 0,
      scroll_percent: 0
    };
  }

  render() {
    window.addEventListener('scroll', (e) => {
      let window_scroll = window.scrollY;
      let screen_height = window.innerHeight;
      let scroll_percent = window_scroll/screen_height;
      this.setState({
        scroll_y: window_scroll,
        screen_y: screen_height,
        scroll_percent: scroll_percent
      });

      window.onbeforeunload = function pushRefresh() {
        window.scrollTo(0, 0);
      }
    });

    return (
      <div className="App">
        <TommMain percent={this.state.scroll_percent}></TommMain>
        <PageIntro percent={this.state.scroll_percent}></PageIntro>
        <PageResult percent={this.state.scroll_percent}></PageResult>
        <PageUpload percent={this.state.scroll_percent}></PageUpload>
        <PageFooter percent={this.state.scroll_percent}></PageFooter>
      </div>
    );
  }
}

export default App;
