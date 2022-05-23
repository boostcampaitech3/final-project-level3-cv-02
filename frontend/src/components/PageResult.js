import React, { Component } from 'react';
import './PageResult.css';
import "slick-carousel/slick/slick.css"
import "slick-carousel/slick/slick-theme.css"
import Slider from "react-slick";

import result_before_01 from '../img/result_before_01.jpeg';
import result_sketch_01 from '../img/result_sketch_01.jpeg';
import result_after_01 from '../img/result_after_01.png';
import sdedit_result from '../img/SDEdit_result.mp4';

class PageResult extends Component {
  render() {
    const settings = {
      dots: true,
      infinite: true,
      speed: 500,
      // slidesToShow: 1,
      // slidesToScroll: 1,
      autoplay: true
    };

    return (
      <div className="Result-background">
        <div className="Carousel-background-block">
          <h2>Our Results</h2>
          <video className="Result-MP4" autoPlay="autoPlay" loop="infinite" muted>
            <source src={sdedit_result}></source>
          </video>
          <Slider {...settings}>
            <div className="Carousel-inside-block">
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
            </div>
            <div className="Carousel-inside-block">
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
              <img src={result_before_01} className="Result-before" alt=""></img>
              <img src={result_sketch_01} className="Result-sketch" alt=""></img>
              <img src={result_after_01} className="Result-after" alt=""></img>
            </div>
          </Slider>
        </div>
      </div>
    );
  }
}

export default PageResult;