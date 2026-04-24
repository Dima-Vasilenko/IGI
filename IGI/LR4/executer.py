import serializer
import regex
import calculating
import geometric
import matrix
import dataanalyzer
import datahandler


class Executer:
    def __init__(self):
        csv_ser = serializer.CsvSerializer("data.csv")
        pickle_ser = serializer.PickleSerializer("data_pickle.bin")
        self.data_1 = serializer.Data(csv_ser)
        self.data_2 = serializer.Data(pickle_ser)

        self.text_analyzer = regex.TextAnalyzer("text.txt")
        graph_builder = calculating.GriphBuilder()
        self.calculator = calculating.Calculating(0.01, graph_builder)


        self.figure_handler = geometric.FigureHandler()
        self.matrix_handler = matrix.MatrixHandker()
        self.analyzer = dataanalyzer.DataAnalyzer()


    def run(self):  
        """Run all required tasks"""
        while(True):
            print("1-е задание", "="*30)
            self.data_1.execute(serializer.user_results)
            self.data_2.execute(serializer.user_results)
            print("="*41)

            print("2-е задание", "="*30)
            self.text_analyzer.save_results("results.txt")
            print("="*41)

            print("3-е задание", "="*30)
            self.calculator.get_results(0.5)
            print("="*41)


            print("4-е задание", "="*30)
            self.figure_handler.accure()
            print("="*41)


            print("5-е задание", "="*30)
            self.matrix_handler.generate_matrix()
            self.matrix_handler.get_results()
            print("="*41)

            print("6-е задание", "="*30)
            self.analyzer.anylyze()
            self.analyzer.average_coast()
            self.analyzer.mpg_comparison()
            print("="*41)

            answer = datahandler.DataHandler.get_int("Введите 1 - если хотите снова запустить работу: ")
            if (answer != 1):
                break