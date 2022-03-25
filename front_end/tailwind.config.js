module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'display':['Open Sans Condensed'],
        'paragraph':['Mirza'],
      },
      colors: {
        'first': '#F6F5F5',
        'second': '#145374',
        'third': '#00334E',
        'fourth': '#EE6F57',
      }
    },
  },
  plugins: [],
}
