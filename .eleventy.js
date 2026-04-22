module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("site/styles.css");

  return {
    dir: {
      input: "site",
      output: "docs"
    }
  };
};
