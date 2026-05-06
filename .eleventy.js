module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("site/styles.css");
  eleventyConfig.addGlobalData("buildDate", new Date());
eleventyConfig.addFilter("formatBuildDate", function(date) {
    if (!date) date = new Date();
    const pad = (n) => n.toString().padStart(2, '0');
    const year = date.getFullYear();
    const month = pad(date.getMonth() + 1);
    const day = pad(date.getDate());
    const hours = pad(date.getHours());
    const minutes = pad(date.getMinutes());
    return `${year}-${month}-${day} ${hours}:${minutes}`;
  });

  return {
    dir: {
      input: "site",
      output: "docs"
    }
  };
};
