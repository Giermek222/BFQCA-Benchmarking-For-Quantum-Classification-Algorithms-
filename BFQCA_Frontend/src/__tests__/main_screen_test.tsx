import MainScreen from "../Components/main_screen";
import * as React from "react";
import { render, screen } from "@testing-library/react";

describe("main Screen components show correctly", () => {
  it("renders Select component", () => {
    render(<MainScreen />);

    expect(screen.getByRole("Select")).toBeInTheDocument();
  });
  it("renders Button component", () => {
    render(<MainScreen />);

    expect(screen.getByRole("Button")).toBeInTheDocument();
  });
});
