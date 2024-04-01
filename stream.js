// for large data files, we can use stream and buffer out data in small chunks and use that buffer data as soon as it is available.
const fs = require('fs');

const readstream = fs.createReadStream('./files/pns.pdf',{encoding: 'utf-8'});
const writestream = fs.createWriteStream('./files/pnswritestream.txt');

readstream.on('data',(chunk)=>{
    console.log('-----------------------------------------new chunk -----------------------------------------------');
    // console.log(chunk.toString());
    writestream.write('\n NEW CHUNK \n');
    writestream.write(chunk);
    console.log('successfully written chunk'); 
})

// we use a pipe to read and write data directly to a file. and above code is much simpler

readstream.pipe(writestream);
