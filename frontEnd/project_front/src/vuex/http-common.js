import axios from "axios";

export default axios.create({
  baseURL: "http://70.12.247.108:8080/",
  headers: {
    "Content-type": "application/json"
  }
});
