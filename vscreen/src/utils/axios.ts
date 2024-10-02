import axios from "axios";

const http = axios.create({ baseURL: "http://127.0.0.1:5000" });

http.interceptors.response.use(
    (res) => { return res.data; },
    (error) => { return Promise.reject(error); }
);

export default http;