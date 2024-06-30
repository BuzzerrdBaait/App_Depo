

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    './**/*.css',
    './**/*.js',

  ],
  theme: {
    extend: {
      colors:{
        rust:{
          500: '#b7410e',
          700: '#8a2b0e',
        },
        carbon: '#2d2d2d'
      }
    },
  },
  plugins: [],
}

