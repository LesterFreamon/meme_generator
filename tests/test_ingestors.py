import os
import unittest

from ..src.models import QuoteModel
from ..src.QuoteEngine.Ingestor import Ingestor
from ..src.QuoteEngine.TXTIngestor import TXTIngestor
from ..src.QuoteEngine.PDFIngestor import PDFIngestor
from ..src.QuoteEngine.DocxIngestor import DocxIngestor
from ..src.QuoteEngine.CSVIngestor import CSVIngestor
from ..src.QuoteEngine.helpers import can_ingest, check_fieldnames


class TestIngestors(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.dir_file_path = os.path.dirname(__file__)
        cls.data_file_path = os.path.join(cls.dir_file_path, 'data')
        cls.csv_file_path = os.path.join(cls.data_file_path, 'csv_file.csv')
        cls.pdf_file_path = os.path.join(cls.data_file_path, 'pdf_file.pdf')
        cls.docx_file_path = os.path.join(cls.data_file_path, 'docx_file.docx')
        cls.txt_file_path = os.path.join(cls.data_file_path, 'txt_file.txt')
        cls.no_file_path = os.path.join(cls.data_file_path, 'no_file.csv')

    def test_check_fieldnames(self):
        with self.assertRaises(ValueError) as e:
            check_fieldnames(['author'])

        self.assertEqual(
            '"body" field could not be found in file', str(e.exception)
        )

        with self.assertRaises(ValueError) as e:
            check_fieldnames(['body'])

        self.assertEqual(
            '"author" field could not be found in file', str(e.exception)
        )

        # should not raise exception
        check_fieldnames(['body', 'author', 'bla'])

    def test_can_ingest(self):
        self.assertTrue(can_ingest(self.csv_file_path, {'.csv'}))

        self.assertFalse(can_ingest(self.csv_file_path, {'.pdf'}))

        self.assertTrue(can_ingest(self.pdf_file_path, {'.pdf'}))

        self.assertTrue(can_ingest(self.docx_file_path, {'.docx'}))

        self.assertTrue(can_ingest(self.txt_file_path, {'.txt'}))

        self.assertFalse(
            can_ingest(self.no_file_path, {'.csv', '.pdf', '.docx', '.txt'})
        )

    def test_csv_ingestor(self):
        good_file_path = self.csv_file_path
        wrong_file_path = self.pdf_file_path

        # Good csv file path
        self.assertTrue(CSVIngestor.can_ingest(good_file_path))
        # bad file path
        self.assertFalse(CSVIngestor.can_ingest(wrong_file_path))
        # no file path
        self.assertFalse(CSVIngestor.can_ingest(self.no_file_path))

        expected_outs = [
            QuoteModel('Skittle', 'Chase the mailman'),
            QuoteModel('Mr. Paws', 'When in doubt, go shoe-shopping')
        ]
        actual_outs = CSVIngestor.parse(good_file_path)
        self.assertEqual(len(expected_outs), len(actual_outs))
        for expected_out, actual_out in zip(expected_outs, actual_outs):
            self.assertEqual(expected_out, actual_out)

        with self.assertRaises(ValueError) as e:
            CSVIngestor.parse(wrong_file_path)

        self.assertEqual(
            '...df_file.pdf does not contain a csv file',
            str(e.exception)
        )

    def test_txt_ingestor(self):
        good_file_path = self.txt_file_path
        wrong_file_path = self.csv_file_path

        # Good txt file path
        self.assertTrue(TXTIngestor.can_ingest(good_file_path))
        # bad file path
        self.assertFalse(TXTIngestor.can_ingest(wrong_file_path))
        # no file path
        self.assertFalse(TXTIngestor.can_ingest(self.no_file_path))

        expected_outs = [
            QuoteModel('Bork', 'To bork or not to bork'),
            QuoteModel('Stinky', 'He who smelt it...')
        ]

        actual_outs = TXTIngestor.parse(good_file_path)
        self.assertEqual(len(expected_outs), len(actual_outs))
        for expected_output, actual_output in zip(expected_outs, actual_outs):
            self.assertEqual(expected_output, actual_output)

        with self.assertRaises(ValueError) as e:
            TXTIngestor.parse(wrong_file_path)

        self.assertEqual(
            '...sv_file.csv does not contain a txt file',
            str(e.exception)
        )

    def test_pdf_ingestor(self):
        good_file_path = self.pdf_file_path
        wrong_file_path = self.docx_file_path

        # Good pdf file path
        self.assertTrue(PDFIngestor.can_ingest(good_file_path))
        # bad file path
        self.assertFalse(PDFIngestor.can_ingest(wrong_file_path))
        # no file path
        self.assertFalse(PDFIngestor.can_ingest(self.no_file_path))

        expected_outs = [
            QuoteModel('Fluffles', 'Treat yo self'),
            QuoteModel('Forrest Pup', 'Life is like a box of treats'),
            QuoteModel('Bark Twain', 'It\'s the size of the fight in the dog')
        ]

        actual_outs = PDFIngestor.parse(good_file_path)
        self.assertEqual(len(expected_outs), len(actual_outs))
        for expected_output, actual_output in zip(expected_outs, actual_outs):
            self.assertEqual(expected_output, actual_output)

        with self.assertRaises(ValueError) as e:
            PDFIngestor.parse(wrong_file_path)

        self.assertEqual(
            '...sv_file.csv does not contain a pdf file',
            str(e.exception)
        )

    def test_docx_ingestor(self):
        good_file_path = self.docx_file_path
        wrong_file_path = self.txt_file_path

        # Good pdf file path
        self.assertTrue(DocxIngestor.can_ingest(good_file_path))
        # bad file path
        self.assertFalse(DocxIngestor.can_ingest(wrong_file_path))
        # no file path
        self.assertFalse(DocxIngestor.can_ingest(self.no_file_path))

        expected_outs = [
            QuoteModel('Rex', 'Bark like no one’s listening'),
            QuoteModel('Chewy', 'RAWRGWAWGGR'),
            QuoteModel('Peanut', 'Life is like peanut butter: crunchy'),
            QuoteModel('Tiny', 'Channel your inner husky')
        ]

        actual_outs = DocxIngestor.parse(good_file_path)
        self.assertEqual(len(expected_outs), len(actual_outs))
        for expected_output, actual_output in zip(expected_outs, actual_outs):
            self.assertEqual(expected_output, actual_output)

        with self.assertRaises(ValueError) as e:
            DocxIngestor.parse(wrong_file_path)

        self.assertEqual(
            '...xt_file.txt does not contain a docx file',
            str(e.exception)
        )

    def test_factory_ingestor(self):
        expected_outs = [
            QuoteModel('Skittle', 'Chase the mailman'),
            QuoteModel('Mr. Paws', 'When in doubt, go shoe-shopping')
        ]
        actual_outs = Ingestor.parse(self.csv_file_path)
        self.assertEqual(len(expected_outs), len(actual_outs))
        for expected_out, actual_out in zip(expected_outs, actual_outs):
            self.assertEqual(expected_out, actual_out)

        self.assertIsNone(Ingestor.parse(self.no_file_path))
