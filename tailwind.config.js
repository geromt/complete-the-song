/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["application/templates/*.html"],
  theme: {
    extend: {
        colors: {
            'rich-black': '#030F11',
            'midnight-green': '#1D4049',
            'pacific-blue': '#50A4B9',
            'dark-sky-blue': '#8AC2D0',
            'blizzard': '#B8E9F4',
            'apple-green': '#8FD694',
            'yellow-red': '#F9C04E',
            'ruby-red': '#DB2763',
        },
        animation: {
        'pulse': 'pulse 8s cubic-bezier(0.4, 0, 0.6, 1) infinite;',
        }
    },
  },
  plugins: [],
}
