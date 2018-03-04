from os import environ
from unittest import TestCase, TestSuite, TextTestRunner

import pgconninfo

class TestDatabaseUrl(TestCase):
    def runTest(self):
        environ['DATABASE_URL'] = 'postgresql://'
        x = pgconninfo.pg_conninfo()
        self.assertEqual(x['HOST'], 'localhost')
        self.assertEqual(x['PORT'], 5432)
        self.assertEqual(x['NAME'], environ['USER'])
        self.assertEqual(x['USER'], environ['USER'])
        self.assertIsNone(x['PASSWORD'])
        self.assertEqual(x['OPTIONS'], {})

        environ['DATABASE_URL'] = 'postgresql://localhost'
        x = pgconninfo.pg_conninfo()
        self.assertEqual(x['HOST'], 'localhost')
        self.assertEqual(x['PORT'], 5432)
        self.assertEqual(x['NAME'], environ['USER'])
        self.assertEqual(x['USER'], environ['USER'])
        self.assertIsNone(x['PASSWORD'])
        self.assertEqual(x['OPTIONS'], {})

        environ['DATABASE_URL'] = 'postgresql://localhost:5433'
        x = pgconninfo.pg_conninfo()
        self.assertEqual(x['HOST'], 'localhost')
        self.assertEqual(x['PORT'], 5433)
        self.assertEqual(x['NAME'], environ['USER'])
        self.assertEqual(x['USER'], environ['USER'])
        self.assertIsNone(x['PASSWORD'])
        self.assertEqual(x['OPTIONS'], {})

        environ['DATABASE_URL'] = 'postgresql://localhost/mydb'
        x = pgconninfo.pg_conninfo()
        self.assertEqual(x['HOST'], 'localhost')
        self.assertEqual(x['PORT'], 5432)
        self.assertEqual(x['NAME'], 'mydb')
        self.assertEqual(x['USER'], environ['USER'])
        self.assertIsNone(x['PASSWORD'])
        self.assertEqual(x['OPTIONS'], {})

        environ['DATABASE_URL'] = 'postgresql://user@localhost'
        x = pgconninfo.pg_conninfo()
        self.assertEqual(x['HOST'], 'localhost')
        self.assertEqual(x['PORT'], 5432)
        self.assertEqual(x['NAME'], environ['USER'])
        self.assertEqual(x['USER'], 'user')
        self.assertIsNone(x['PASSWORD'])
        self.assertEqual(x['OPTIONS'], {})

        environ['DATABASE_URL'] = 'postgresql://user:secret@localhost'
        x = pgconninfo.pg_conninfo()
        self.assertEqual(x['HOST'], 'localhost')
        self.assertEqual(x['PORT'], 5432)
        self.assertEqual(x['NAME'], environ['USER'])
        self.assertEqual(x['USER'], 'user')
        self.assertEqual(x['PASSWORD'], 'secret')
        self.assertEqual(x['OPTIONS'], {})

        environ['DATABASE_URL'] = 'postgresql://other@localhost/otherdb?connect_timeout=10&application_name=myapp'
        x = pgconninfo.pg_conninfo()
        self.assertEqual(x['HOST'], 'localhost')
        self.assertEqual(x['PORT'], 5432)
        self.assertEqual(x['NAME'], 'otherdb')
        self.assertEqual(x['USER'], 'other')
        self.assertIsNone(x['PASSWORD'])
        self.assertEqual(x['OPTIONS'], {
            'connect_timeout': ['10'],
            'application_name': ['myapp'],
        })

if __name__ == '__main__':
    runner = TextTestRunner()
    runner.run(TestDatabaseUrl())
