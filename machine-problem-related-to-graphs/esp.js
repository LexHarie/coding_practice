const fs = require("fs");

fs.readFile("schedule.txt", "utf8", (err, data) => {
  if (err) {
    console.error("Error reading the file:", err);
    return;
  }

  const courses = {};

  const lines = data.split("\n");

  lines.forEach((line) => {
    if (line.trim() !== "") {
      const parts = line.split(" ");

      courses[parts[0]] = parts.slice(1);
    }
  });

  let n = Object.keys(courses).length;
  let matrix = Array(n)
    .fill(null)
    .map(() => Array(n).fill(0));

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let course1 = Object.keys(courses)[i];
      let course2 = Object.keys(courses)[j];
      for (let student of courses[course1]) {
        if (courses[course2].includes(student)) {
          matrix[i][j] = 1;
          matrix[j][i] = 1;
          break;
        }
      }
    }
  }

  let colors = Array(n).fill(-1);

  let getAvailableColors = (vertex) => {
    let adjacentColors = new Set();
    for (let i = 0; i < n; i++) {
      if (matrix[vertex][i] && colors[i] !== -1) {
        adjacentColors.add(colors[i]);
      }
    }
    for (let i = 0; i < n; i++) {
      if (!adjacentColors.has(i)) return i;
    }
  };

  for (let i = 0; i < n; i++) {
    if (colors[i] === -1) {
      let color = getAvailableColors(i);
      colors[i] = color;
      for (let j = 0; j < n; j++) {
        if (i !== j && colors[j] === -1 && matrix[i][j] === 0) {
          let canUseSameColor = true;
          for (let k = 0; k < n; k++) {
            if (matrix[j][k] && colors[k] === color) {
              canUseSameColor = false;
              break;
            }
          }
          if (canUseSameColor) colors[j] = color;
        }
      }
    }
  }

  let courseKeys = Object.keys(courses);
  console.log("\t" + courseKeys.join("\t"));
  for (let i = 0; i < n; i++) {
    let row = [courseKeys[i]].concat(matrix[i]);
    console.log(row.join("\t"));
  }

  console.log("Schedule of exams");
  let scheduleFormat = [
    "Monday 8:30 - 11:30 AM",
    "Monday 1:00 - 4:00 PM",
    "Tuesday 8:30 - 11:30 AM",
    "Tuesday 1:00 - 4:00 PM",
  ];

  for (let i = 0; i < scheduleFormat.length; i++) {
    let coursesWithSameColor = [];
    for (let j = 0; j < n; j++) {
      if (colors[j] === i) {
        coursesWithSameColor.push(courseKeys[j]);
      }
    }
    console.log(scheduleFormat[i] + ":", coursesWithSameColor.join(", "));
  }
});
