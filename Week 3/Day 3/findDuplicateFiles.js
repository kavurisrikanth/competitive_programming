const fs = require('fs')

function findDuplicateFiles(startingDirectory) {
  let seen = {},
      stack = [startingDirectory],
      ans = [];

  while (stack.length) {
    let thisPath = stack.pop(),
        thisFile = fs.statSync(thisPath);

    // if its a directory,
    // put the contents in our stack

    if (thisFile.isDirectory()) {
      fs.readdirSync(thisPath).forEach((path) => {
        stack.push(thisPath + '/' + path);
      });
      
    } else {
      // if it's a file, get its contents and its last edited time
      let fileContents = fs.readFileSync(thisPath),
          lastEditedTime = thisFile.mtime;

      if(seen.hasOwnProperty(fileContents)){
        //if we've seen it before
        let currentFile = seen[fileContents];
        
        if (lastEditedTime > currentFile.lastEditedTime) {
          //current file is the dupe!
          ans.push([thisPath, currentFile.path]);
        } else {
          //old file is the dupe!
          ans.push([currentFile.path, thisPath]);
          //but also update seen to have the new file's info
          seen[fileContents] = {lastEditedTime: lastEditedTime, path: thisPath}
        }
        
      // if it's a new file, record its path
      } else {
        seen[fileContents] = {lastEditedTime: lastEditedTime, path: thisPath}
      }
    }
  }
  return ans;
}