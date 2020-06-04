import React,{Component,useState} from 'react';
import { Modal } from 'react-bootstrap'

const Login = () => (
  <Modal  bsSize="large">
    <Modal.Header closeButton>
      <Modal.Title id="contained-modal-title-lg">Modal title</Modal.Title>
    </Modal.Header>
    <Modal.Body>
      <h4>Edit Item</h4>
      <input
        type="text"
        name="name"
      />
      <input
        type="number"
        name="age"
      />
    </Modal.Body>
    <Modal.Footer />
  </Modal>
)

export default Login;

