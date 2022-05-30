import React, { Component } from 'react';
import './PageUpload.css';
import axios from 'axios';
import {ToastsContainer, ToastsStore, ToastsContainerPosition} from 'react-toasts';
import file_upload_img from '../img/file_upload_img.png';
import logo_brown from '../img/logo_brown.png';

class PageUpload extends Component {
    constructor(props){
      super(props);
      this.state={
        email: '',
        original_image_file: null,
        sketch_image_file: null,
        original_image_url: file_upload_img,
        sketch_image_url: file_upload_img,
        original_image_size: null,
        sketch_image_size: null
      }
      this.inputEmailHandler = this.inputEmailHandler.bind(this)
      this.inputImageHandler = this.inputImageHandler.bind(this)
      this.inputSubmitHandler = this.inputSubmitHandler.bind(this)
    }
    inputEmailHandler(e) {
      e.preventDefault();
      this.setState({email: e.target.value})
    }
    inputImageHandler(e) {
      e.preventDefault();
      var file = e.target.files[0];
      var target_name = e.target.name + '_url';
      var file_name = e.target.name + '_file';
      var size_name = e.target.name + '_size';
      var new_url = URL.createObjectURL(file);
      var img = new Image();
      img.src = new_url;
      img.onload = function() {
        this.setState({
          [target_name]: new_url,
          [file_name]: file,
          [size_name]: [img.width, img.height]
        });
      }.bind(this);
    }
    inputSubmitHandler(e) {
      e.preventDefault();
      let original_img_url = this.state.original_image_url;
      let sketch_img_url = this.state.sketch_image_url;
      let current_time = new Date();
      let time = {
        year: current_time.getFullYear(),
        month: current_time.getMonth()+1,
        date: current_time.getDate(),
        hours: current_time.getHours(),
        minutes: current_time.getMinutes()
      };
      let timestring = `${time.year}/${time.month}/${time.date} ${time.hours}:${time.minutes}`;

      if (this.state.original_image_file===null) { 
          ToastsStore.success("원본 이미지를 업로드해주세요");
       }
      else if (this.state.sketch_image_file===null) {
          ToastsStore.success("스케치 이미지를 업로드해주세요");
      }
      else if (this.state.email==='') {
          ToastsStore.success("이메일을 입력해주세요");
      }
      else {
        const data = new FormData();
        var host = window.location.protocol + "//" + window.location.host + "api/image";

        data.append('submit_original_img', this.state.original_image_file);
        data.append('submit_sketch_img', this.state.sketch_image_file);
        data.append('submit_email', this.state.email);
        data.append('original_image_size', this.state.original_image_size);
        data.append('sketch_image_size', this.state.sketch_image_size);
        data.append('upload_time', timestring);

        axios.post(host, data, {
          onUploadProgress: ProgressEvent => {
            this.setState({
              loaded: (ProgressEvent.loaded / ProgressEvent.total*100),
            })
          },
        }) 
        ToastsStore.success("업로드 완료 :) 1시간 뒤 메일함을 확인해주세요!");
      
        this.setState({
          email: '',
          original_image_file: null,
          sketch_image_file: null,
          original_image_url: file_upload_img,
          sketch_image_url: file_upload_img,
          original_image_size: null,
          sketch_image_size: null
        });
        URL.revokeObjectURL(original_img_url);
        URL.revokeObjectURL(sketch_img_url);
      }
    }

    render() {
      return (
        <div 
          className={(this.props.percent > 3.8) ? "Upload-background" : "Upload-background-ani"}
          id="scroll_to_upload">
          <img src={logo_brown} className="Upload-logo" alt=""></img>
          <h2 className="Upload-background-title">내일의 집 꾸며보기</h2>
          <form 
            className="Upload-form"
            action="/" 
            method="post"
            onSubmit={this.inputSubmitHandler}>

            <div className="Upload-original">
              <h2 className="Upload-title">원본 사진</h2>
              <label id="Upload-original-sub" htmlFor="Upload-original-button">
                <img src={this.state.original_image_url} className="File-upload-img" alt=""></img>
              </label>
              <input 
                type="file"
                id="Upload-original-button"
                accept="image/*"
                name='original_image'
                onChange={this.inputImageHandler}>
              </input>
            </div>
            <div className="Upload-sketch">
              <h2 className="Upload-title">스케치 사진</h2>
              <label id="Upload-sketch-sub" htmlFor="Upload-sketch-button">
                <img src={this.state.sketch_image_url} className="File-upload-img" alt=""></img>
              </label>
              <input 
                type="file"
                id="Upload-sketch-button"
                accept="image/jpg, image/jpeg, image/png"
                name='sketch_image'
                onChange={this.inputImageHandler}>
              </input>
            </div>
            <input
              className="Upload-email"
              type="text"
              placeholder={'이메일을 입력하세요'}
              value={this.state.email}
              onChange={this.inputEmailHandler}
            ></input>
            <input
              className="Upload-submit"
              type="submit"
              value="완료"
            ></input>
            <ToastsContainer 
              position={ToastsContainerPosition.BOTTOM_CENTER} store={ToastsStore} lightBackground/>
          </form>
        </div>
      );
    }
}

export default PageUpload;