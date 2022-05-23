import React, { Component } from 'react';
import './TommMain.css';
import main_image from '../img/main_sketch.png';
import main_logo from '../img/main_logo.png';

class TommMain extends Component {
  constructor(props) {
    super(props);
    this.state = {
      main_text: 'PERSONAL INTERIOR\nCONSULTING',
      sub_text: '\nBucket-Interior',
      button_text: 'Start'
    }
  }
    render() {
      return (
        <div className="Main-background">
          <img src={main_logo} className="Main-Logo" alt=""></img>
          <img src={main_image} className="Main-Image" alt=""></img>
          <div className="Main-Text-Div-01">
            <text className="Main-Text-01">{this.state.main_text}</text>
            <text className="Main-Text-02">{this.state.sub_text}</text>
          </div>
          <div className="Main-Button-Div-01">
            <button className="Main-Button-01">{this.state.button_text}</button>
          </div>

          
        </div>
      );
    }
}

export default TommMain;