import React, { Component } from 'react';
import './PageResult.css';
import "slick-carousel/slick/slick.css"
import "slick-carousel/slick/slick-theme.css"
import Slider from "react-slick";
import sdedit_result from '../img/SDEdit_result.mp4';

class PageResult extends Component {
  render() {
    const settings = {
      dots: true,
      infinite: true,
      speed: 800,
      autoplay: true,
      autoplaySpeed: 3000,
      arrows: false,
      pauseOnHover: true
    };

    return (
      <div className={(this.props.percent > 2.5) ? "Result-background" : "Result-background-ani"} id="scroll_to_result">
        <div className="Carousel-background-block">
          <h2>SDEdit & Our Results</h2>
          <video className="Result-MP4" autoPlay="autoPlay" loop="infinite" muted>
            <source src={sdedit_result}></source>
          </video>
          <Slider {...settings}>
            <div className="Carousel-inside-block">
              <img src={require('../img/sdedit_results/result_08_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_08_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_08_generated.png')} className="Result-after" alt=""></img>
              <img src={require('../img/sdedit_results/result_11_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_11_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_11_generated.png')} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={require('../img/sdedit_results/result_06_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_06_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_06_generated.png')} className="Result-after" alt=""></img>
              <img src={require('../img/sdedit_results/result_09_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_09_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_09_generated.png')} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={require('../img/sdedit_results/result_07_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_07_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_07_generated.png')} className="Result-after" alt=""></img>
              <img src={require('../img/sdedit_results/result_04_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_04_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_04_generated.png')} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={require('../img/sdedit_results/result_05_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_05_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_05_generated.png')} className="Result-after" alt=""></img>
              <img src={require('../img/sdedit_results/result_01_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_01_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_01_generated.png')} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={require('../img/sdedit_results/result_03_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_03_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_03_generated.png')} className="Result-after" alt=""></img>
              <img src={require('../img/sdedit_results/result_10_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_10_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_10_generated.png')} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={require('../img/sdedit_results/result_02_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_02_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_02_generated.png')} className="Result-after" alt=""></img>
              <img src={require('../img/sdedit_results/result_12_original.png')} className="Result-before" alt=""></img>
              <img src={require('../img/sdedit_results/result_12_sketch.png')} className="Result-sketch" alt=""></img>
              <img src={require('../img/sdedit_results/result_12_generated.png')} className="Result-after" alt=""></img>
            </div>
          </Slider>
        </div>
      </div>
    );
  }
}

export default PageResult;