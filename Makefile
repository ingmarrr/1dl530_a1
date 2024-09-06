#
# # example Makefile to build an executable named myprog from myprog.cpp
# #

PROG=performance
SHARED_VAR=shared-variable

run: all
	@./bin/$(PROG)

# for i in {0..10}; \
# 	do echo Iteration $i >> output.txt; \
# 	make exec-shared-variable >> output-shared-variable.txt; \
# 	echo "\n" >> output-shared-variable.txt; \
# done \

all: $(PROG).cpp
	@g++ -std=c++11 -Wall -pthread $(PROG).cpp -o bin/$(PROG)

clean:
	$(RM) $(PROG)

watch-report:report.tex
	@fswatch report.tex | xargs -n 1 -I {} make report

report:report.tex
	@pdflatex report.tex
	@pdflatex report.tex
	# @make clean-tex

clean-tex:
	@rm -f *.aux *.log *.toc *.blg *.out *.bbl
