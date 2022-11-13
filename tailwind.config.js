/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/*.html"],
  theme: {
    extend: {
        animation: {
        'pulse': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite;',
      }
    },
    colors: {
        'space': '#3F4A59',
        'tea-green': '#DBF7CB',
        'sea-green': '#A3E3C6',
        'green-sheen': '#64B5B0',
    }
  },
  plugins: [],
}
