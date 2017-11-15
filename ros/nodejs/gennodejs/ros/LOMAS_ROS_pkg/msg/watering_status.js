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

class watering_status {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Watering = null;
      this.Interval = null;
      this.Duration = null;
      this.Zones = null;
      this.ErrorNr = null;
      this.StartTime = null;
      this.FinishedTime = null;
    }
    else {
      if (initObj.hasOwnProperty('Watering')) {
        this.Watering = initObj.Watering
      }
      else {
        this.Watering = false;
      }
      if (initObj.hasOwnProperty('Interval')) {
        this.Interval = initObj.Interval
      }
      else {
        this.Interval = 0;
      }
      if (initObj.hasOwnProperty('Duration')) {
        this.Duration = initObj.Duration
      }
      else {
        this.Duration = 0;
      }
      if (initObj.hasOwnProperty('Zones')) {
        this.Zones = initObj.Zones
      }
      else {
        this.Zones = 0;
      }
      if (initObj.hasOwnProperty('ErrorNr')) {
        this.ErrorNr = initObj.ErrorNr
      }
      else {
        this.ErrorNr = 0;
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
    // Serializes a message object of type watering_status
    // Serialize message field [Watering]
    bufferOffset = _serializer.bool(obj.Watering, buffer, bufferOffset);
    // Serialize message field [Interval]
    bufferOffset = _serializer.uint8(obj.Interval, buffer, bufferOffset);
    // Serialize message field [Duration]
    bufferOffset = _serializer.uint8(obj.Duration, buffer, bufferOffset);
    // Serialize message field [Zones]
    bufferOffset = _serializer.uint8(obj.Zones, buffer, bufferOffset);
    // Serialize message field [ErrorNr]
    bufferOffset = _serializer.uint8(obj.ErrorNr, buffer, bufferOffset);
    // Serialize message field [StartTime]
    bufferOffset = _serializer.time(obj.StartTime, buffer, bufferOffset);
    // Serialize message field [FinishedTime]
    bufferOffset = _serializer.time(obj.FinishedTime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type watering_status
    let len;
    let data = new watering_status(null);
    // Deserialize message field [Watering]
    data.Watering = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [Interval]
    data.Interval = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [Duration]
    data.Duration = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [Zones]
    data.Zones = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [ErrorNr]
    data.ErrorNr = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [StartTime]
    data.StartTime = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [FinishedTime]
    data.FinishedTime = _deserializer.time(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 21;
  }

  static datatype() {
    // Returns string type for a message object
    return 'LOMAS_ROS_pkg/watering_status';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'aa9f746190ed194acba95f06be5c0be9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool Watering
    uint8 Interval
    uint8 Duration
    uint8 Zones
    uint8 ErrorNr
    time StartTime
    time FinishedTime
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new watering_status(null);
    if (msg.Watering !== undefined) {
      resolved.Watering = msg.Watering;
    }
    else {
      resolved.Watering = false
    }

    if (msg.Interval !== undefined) {
      resolved.Interval = msg.Interval;
    }
    else {
      resolved.Interval = 0
    }

    if (msg.Duration !== undefined) {
      resolved.Duration = msg.Duration;
    }
    else {
      resolved.Duration = 0
    }

    if (msg.Zones !== undefined) {
      resolved.Zones = msg.Zones;
    }
    else {
      resolved.Zones = 0
    }

    if (msg.ErrorNr !== undefined) {
      resolved.ErrorNr = msg.ErrorNr;
    }
    else {
      resolved.ErrorNr = 0
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

module.exports = watering_status;
