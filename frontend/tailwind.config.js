/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          mint: "#00CB98",
          turquoise: "#00C8B3",
        },
        surface: {
          authBg: "#111827",
          dark: "#1E2530",
          light: "#FFFFFF",
          page: "#F3F4F6",
          subtle: "#F9FAFB",
          border: "var(--color-border-dark)",
          borderLight: "var(--color-border-light)",
        },
        ink: {
          secondary: "var(--color-ink-secondary)",
          mutedDark: "var(--color-ink-muted-dark)",
          placeholder: "#8892A2",
        },
        control: {
          disabled: "#D1D6DE",
        },
        status: {
          pending: "#EAB308",
          analysisBlue: "#3B82F6",
          analysisBlueAlt: "#3182CE",
          inProgress: "#F97316",
          inProgressBg: "#F6D8C4",
          doneBg: "#D1FAE5",
          doneText: "#065F46",
          indigoBg: "#E0E7FF",
          indigoText: "#3730A3",
        },
        overlay: "rgb(15 23 42 / <alpha-value>)",
      },
    },
  },
  plugins: [],
};
