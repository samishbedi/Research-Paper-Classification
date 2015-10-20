for file in *.pdf;
do pdf2txt.py -o ${file%.*}.txt $file;
done

