import * as React from "react";
import { render, screen } from "@testing-library/react";
import LoginScreen from "../Components/login_screen";
import { Router, Routes } from "react-router-dom";
import { Provider } from "react-redux";
describe("Login Screen", () => {
  it("renders buttons component", () => {
    render(<LoginScreen />);

    expect(screen.getByRole("Button")).toBeInTheDocument();
  });

  it("renders textField component", () => {
    render(<LoginScreen />);

    expect(screen.getByRole("TextField")).toBeInTheDocument();
  });
});

test("renders learn react link", () => {
  const { getByText } = render(
    <Provider>
      <LoginScreen />
    </Provider>
  );
  expect(getByText(/Hello/i)).toBeInTheDocument();
});
