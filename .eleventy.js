module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("site/styles.css");
  eleventyConfig.addPassthroughCopy("site/CNAME");
  eleventyConfig.addPassthroughCopy("Downloads");
  eleventyConfig.addFilter("formatBuildDate", function(date) {
    if (!date) date = new Date();
    // Format using Hungary's timezone (CET/CEST)
    const formatter = new Intl.DateTimeFormat('hu-HU', {
      timeZone: 'Europe/Budapest',
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    });
    const parts = formatter.formatToParts(date);
    const year = parts.find(p => p.type === 'year').value;
    const month = parts.find(p => p.type === 'month').value;
    const day = parts.find(p => p.type === 'day').value;
    const hour = parts.find(p => p.type === 'hour').value;
    const minute = parts.find(p => p.type === 'minute').value;
    return `${year}-${month}-${day} ${hour}:${minute}`;
  });

  return {
    dir: {
      input: "site",
      output: "_site"
    }
  };
};
