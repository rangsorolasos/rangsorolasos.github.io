// site/_data/activists.js
module.exports = async function() {
  const response = await fetch('https://reform.kodekonveyor.com/_data/activists.json');
  if (!response.ok) {
    throw new Error(`HTTP hiba: ${response.status}`);
  }
  return response.json();
};
