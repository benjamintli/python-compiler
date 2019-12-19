llc -filetype=obj ../../output_files/output.ll
gcc -no-pie ../../output_files/output.o -o output
./output