/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f5f7ff',
          100: '#eaeefe',
          200: '#cdd6fd',
          300: '#a9b6fb',
          400: '#7b8bf8',
          500: '#4f5ff5',
          600: '#3745d9',
          700: '#2a36a9',
          800: '#222c85',
          900: '#1f286e'
        }
      },
      boxShadow: {
        soft: '0 10px 25px -5px rgba(0,0,0,0.05), 0 8px 10px -6px rgba(0,0,0,0.05)'
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography')
  ],
}
