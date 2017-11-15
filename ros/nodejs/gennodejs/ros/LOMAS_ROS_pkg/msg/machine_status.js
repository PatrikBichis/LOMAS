// Auto-generated. Do not edit!

// (in-package LOMAS_ROS_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class machine_status {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.IsSynced = null;
      this.SequensStarted = null;
      this.MachineMoving = null;
      this.SequenseNr = null;
      this.ErrorNr = null;
      this.Interval = null;
      this.X = null;
      this.Y = null;
      this.Z = null;
      this.StartTime = null;
      this.FinishedTime = null;
    }
    else {
      if (initObj.hasOwnProperty('IsSynced')) {
        this.IsSynced = initObj.IsSynced
      }
      else {
        this.IsSynced = false;
      }
      if (initObj.hasOwnProperty('SequensStarted')) {
        this.SequensStarted = initObj.SequensStarted
      }
      else {
        this.SequensStarted = false;
      }
      if (initObj.hasOwnProperty('MachineMoving')) {
        this.MachineMoving = initObj.MachineMoving
      }
      else {
        this.MachineMoving = false;
      }
      if (initObj.hasOwnProperty('SequenseNr')) {
        this.SequenseNr = initObj.SequenseNr
      }
      else {
        this.SequenseNr = 0;
      }
      if (initObj.hasOwnProperty('ErrorNr')) {
        this.ErrorNr = initObj.ErrorNr
      }
      else {
        this.ErrorNr = 0;
      }
      if (initObj.hasOwnProperty('Interval')) {
        this.Interval = initObj.Interval
      }
      else {
        this.Interval = 0;
      }
      if (initObj.hasOwnProperty('X')) {
        this.X = initObj.X
      }
      else {
        this.X = 0.0;
      }
      if (initObj.hasOwnProperty('Y')) {
        this.Y = initObj.Y
      }
      else {
        this.Y = 0.0;
      }
      if (initObj.hasOwnProperty('Z')) {
        this.Z = initObj.Z
      }
      else {
        this.Z = 0.0;
      }
      if (initObj.hasOwnProperty('StartTime')) {
        this.StartTime = initObj.StartTime
      }
      else {
        this.StartTime = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('FinishedTime')) {
        this.FinishedTime = initObj.FinishedTime
      }
      else {
        this.FinishedTime = {secs: 0, nsecs: 0};
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type machine_status
    // Serialize message field [IsSynced]
    bufferOffset = _serializer.bool(obj.IsSynced, buffer, bufferOffset);
    // Serialize message field [SequensStarted]
    bufferOffset = _serializer.bool(obj.SequensStarted, buffer, bufferOffset);
    // Serialize message field [MachineMoving]
    bufferOffset = _serializer.bool(obj.MachineMoving, buffer, bufferOffset);
    // Serialize message field [SequenseNr]
    bufferOffset = _serializer.uint8(obj.SequenseNr, buffer, bufferOffset);
    // Serialize message field [ErrorNr]
    bufferOffset = _serializer.uint8(obj.ErrorNr, buffer, bufferOffset);
    // Serialize message field [Interval]
    bufferOffset = _serializer.uint16(obj.Interval, buffer, bufferOffset);
    // Serialize message field [X]
    bufferOffset = _serializer.float32(obj.X, buffer, bufferOffset);
    // Serialize message field [Y]
    bufferOffset = _serializer.float32(obj.Y, buffer, bufferOffset);
    // Serialize message field [Z]
    bufferOffset = _serializer.float32(obj.Z, buffer, bufferOffset);
    // Serialize message field [StartTime]
    bufferOffset = _serializer.time(obj.StartTime, buffer, bufferOffset);
    // Serialize message field [FinishedTime]
    bufferOffset = _serializer.time(obj.FinishedTime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type machine_status
    let len;
    let data = new machine_status(null);
    // Deserialize message field [IsSynced]
    data.IsSynced = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [SequensStarted]
    data.SequensStarted = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [MachineMoving]
    data.MachineMoving = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [SequenseNr]
    data.SequenseNr = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ErrorNr]
    data.ErrorNr = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [Interval]
    data.Interval = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [X]
    data.X = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [Y]
    data.Y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [Z]
    data.Z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [StartTime]
    data.StartTime = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [FinishedTime]
    data.FinishedTime = _deserializer.time(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 35;
  }

  static datatype() {
    // Returns string type for a message object
    return 'LOMAS_ROS_pkg/machine_status';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ac9d44262cab47a9a9d9de2d4f926f62';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool  IsSynced
    bool  SequensStarted
    bool  MachineMoving
    uint8 SequenseNr
    uint8 ErrorNr
    uint16 Interval
    float32 X
    float32 Y
    float32 Z
    time StartTime
    time FinishedTime
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new machine_status(null);
    if (msg.IsSynced !== undefined) {
      resolved.IsSynced = msg.IsSynced;
    }
    else {
      resolved.IsSynced = false
    }

    if (msg.SequensStarted !== undefined) {
      resolved.SequensStarted = msg.SequensStarted;
    }
    else {
      resolved.SequensStarted = false
    }

    if (msg.MachineMoving !== undefined) {
      resolved.MachineMoving = msg.MachineMoving;
    }
    else {
      resolved.MachineMoving = false
    }

    if (msg.SequenseNr !== undefined) {
      resolved.SequenseNr = msg.SequenseNr;
    }
    else {
      resolved.SequenseNr = 0
    }

    if (msg.ErrorNr !== undefined) {
      resolved.ErrorNr = msg.ErrorNr;
    }
    else {
      resolved.ErrorNr = 0
    }

    if (msg.Interval !== undefined) {
      resolved.Interval = msg.Interval;
    }
    else {
      resolved.Interval = 0
    }

    if (msg.X !== undefined) {
      resolved.X = msg.X;
    }
    else {
      resolved.X = 0.0
    }

    if (msg.Y !== undefined) {
      resolved.Y = msg.Y;
    }
    else {
      resolved.Y = 0.0
    }

    if (msg.Z !== undefined) {
      resolved.Z = msg.Z;
    }
    else {
      resolved.Z = 0.0
    }

    if (msg.StartTime !== undefined) {
      resolved.StartTime = msg.StartTime;
    }
    else {
      resolved.StartTime = {secs: 0, nsecs: 0}
    }

    if (msg.FinishedTime !== undefined) {
      resolved.FinishedTime = msg.FinishedTime;
    }
    else {
      resolved.FinishedTime = {secs: 0, nsecs: 0}
    }

    return resolved;
    }
};

module.exports = machine_status;
