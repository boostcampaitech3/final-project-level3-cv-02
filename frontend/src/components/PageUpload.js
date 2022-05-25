import React, { Component } from 'react';
import './PageUpload.css';
import file_upload_img from '../img/file_upload_img.png';
import axios from 'axios';
import { toHaveStyle } from '@testing-library/jest-dom/dist/matchers';

class PageUpload extends Component {
    constructor(props){
      super(props);
      this.state={
        email: '',
        original_image_file: null,
        sketch_image_file: null,
        original_image_url: file_upload_img,
        sketch_image_url: file_upload_img,
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
      var new_url = URL.createObjectURL(file);
      this.setState({
        [target_name]: new_url,
        [file_name]: file
      });
    }
    inputSubmitHandler(e) {
      e.preventDefault();
      alert('Submit!');
      let original_img_url = this.state.original_image_url;
      let sketch_img_url = this.state.sketch_image_url;
      // let submit_original_img = this.state.original_image_file;
      // let submit_sketch_img = this.state.sketch_image_file;
      // let submit_email = this.state.email;

      // FormData로 host에 전송하는 코드?
      const data = new FormData();
      var host = window.location.protocol + "//" + window.location.host + "api/image";
      data.append('submit_original_img', this.state.original_image_file);
      data.append('submit_sketch_img', this.state.sketch_image_file);
      data.append('submit_email', this.state.email);
      axios.post(host, data, {
        onUploadProgress: ProgressEvent => {
          this.setState({
            loaded: (ProgressEvent.loaded / ProgressEvent.total*100),
          })
        },
      }) 
      .then(res => {
        alert('upload success');
      })
      .catch(err => {
        alert('upload fail');
      })
      
      this.setState({
        email: '',
        original_image_file: null,
        sketch_image_file: null,
        original_image_url: file_upload_img,
        sketch_image_url: file_upload_img,
      });
      URL.revokeObjectURL(original_img_url);
      URL.revokeObjectURL(sketch_img_url);
    }

    render() {
      return (
        <div className="Upload-background">
          <h2 className="Upload-title">컨설팅 받아보기</h2>
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
          </form>
        </div>
      );
    }
}

export default PageUpload;