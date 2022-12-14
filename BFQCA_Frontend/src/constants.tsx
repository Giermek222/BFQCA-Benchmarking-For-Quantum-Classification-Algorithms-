const backend = "http://localhost:3001";
const benchmarkGetEndpoint = backend + "/benchmarks/get";
const algorithmExecuteEndpoint = backend + "/algorithms/execute";
const algorithmsGetEndpoint = backend + "/algorithms/get";
const userLoginEndpoint = backend + "/user/login";
const userRegisterEndpoint = backend + "/user/register";

export {
  backend,
  benchmarkGetEndpoint,
  algorithmsGetEndpoint,
  algorithmExecuteEndpoint,
  userLoginEndpoint,
  userRegisterEndpoint,
};
