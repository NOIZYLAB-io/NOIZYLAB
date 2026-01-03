import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
    DB_SYSTEMS_DB: D1Database;
    DB_CACHE: KVNamespace;
    AI: any;
}

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// ==============================================================================
// NOIZYLAB OS - DATABASE SYSTEMS WORKER
// Complete History of Databases from Hierarchical to Modern
// ==============================================================================

const DATABASE_SYSTEMS = {
    // ===========================================================================
    // RELATIONAL DATABASES (RDBMS)
    // ===========================================================================
    relational: {
        ibm_system_r: {
            name: 'IBM System R',
            year: 1974,
            developer: 'IBM',
            significance: 'First SQL implementation, research prototype'
        },
        oracle: {
            name: 'Oracle Database',
            year: 1979,
            developer: 'Larry Ellison, Bob Miner, Ed Oates',
            company: 'Oracle Corporation',
            significance: 'Enterprise database leader',
            versions: ['Oracle 2 (1979)', 'Oracle 7 (1992)', 'Oracle 8i (1999)', 'Oracle 12c (2013)', 'Oracle 19c (2019)', 'Oracle 23ai (2024)'],
            features: ['RAC', 'Data Guard', 'PL/SQL', 'Partitioning', 'In-Memory', 'Autonomous']
        },
        db2: {
            name: 'IBM Db2',
            year: 1983,
            developer: 'IBM',
            significance: 'IBM enterprise database',
            platforms: ['z/OS', 'LUW (Linux/Unix/Windows)', 'iSeries']
        },
        sql_server: {
            name: 'Microsoft SQL Server',
            year: 1989,
            developer: 'Sybase/Microsoft',
            significance: 'Windows enterprise standard',
            versions: ['SQL Server 4.2 (1992)', 'SQL Server 7.0 (1998)', 'SQL Server 2000', '2005', '2008', '2012', '2016', '2017', '2019', '2022'],
            features: ['T-SQL', 'Always On', 'ColumnStore', 'In-Memory OLTP']
        },
        postgresql: {
            name: 'PostgreSQL',
            year: 1996,
            predecessor: 'Ingres/POSTGRES',
            developer: 'Michael Stonebraker (original)',
            significance: 'Most advanced open-source RDBMS',
            features: ['MVCC', 'Extensions', 'JSON/JSONB', 'Full-text search', 'PostGIS', 'Logical replication']
        },
        mysql: {
            name: 'MySQL',
            year: 1995,
            developers: ['Michael Widenius', 'David Axmark'],
            company: 'Oracle (acquired)',
            significance: 'Most popular open-source database',
            engines: ['InnoDB', 'MyISAM', 'Memory', 'Archive'],
            forks: ['MariaDB', 'Percona Server']
        },
        mariadb: {
            name: 'MariaDB',
            year: 2009,
            developer: 'Michael Widenius',
            significance: 'MySQL fork, community-driven',
            features: ['Galera Cluster', 'ColumnStore', 'Spider', 'MaxScale']
        },
        sqlite: {
            name: 'SQLite',
            year: 2000,
            developer: 'D. Richard Hipp',
            significance: 'Most deployed database in the world (embedded)',
            useCases: ['Mobile apps', 'Browsers', 'IoT', 'Embedded systems']
        },
        cockroachdb: {
            name: 'CockroachDB',
            year: 2015,
            company: 'Cockroach Labs',
            significance: 'Distributed SQL, survives failures',
            features: ['Distributed transactions', 'Geo-partitioning', 'PostgreSQL compatible']
        },
        tidb: {
            name: 'TiDB',
            year: 2015,
            company: 'PingCAP',
            significance: 'NewSQL, MySQL compatible, HTAP'
        },
        yugabyte: {
            name: 'YugabyteDB',
            year: 2016,
            significance: 'Distributed SQL, PostgreSQL compatible'
        },
        planetscale: {
            name: 'PlanetScale',
            year: 2018,
            base: 'Vitess (MySQL)',
            significance: 'Serverless MySQL with branching'
        },
        neon: {
            name: 'Neon',
            year: 2022,
            significance: 'Serverless PostgreSQL with branching'
        },
        supabase: {
            name: 'Supabase',
            year: 2020,
            significance: 'Open-source Firebase alternative (PostgreSQL)'
        }
    },

    // ===========================================================================
    // NOSQL - DOCUMENT DATABASES
    // ===========================================================================
    document: {
        mongodb: {
            name: 'MongoDB',
            year: 2009,
            developer: '10gen/MongoDB Inc',
            significance: 'Most popular document database',
            features: ['BSON', 'Aggregation pipeline', 'Atlas', 'Realm', 'Change streams']
        },
        couchdb: {
            name: 'Apache CouchDB',
            year: 2005,
            developer: 'Damien Katz',
            significance: 'Multi-master replication',
            features: ['HTTP API', 'MapReduce views', 'Multi-version concurrency']
        },
        couchbase: {
            name: 'Couchbase',
            year: 2011,
            significance: 'High-performance document store',
            features: ['N1QL (SQL for JSON)', 'Cross-datacenter replication']
        },
        firestore: {
            name: 'Cloud Firestore',
            year: 2017,
            developer: 'Google',
            significance: 'Firebase document database'
        },
        dynamodb: {
            name: 'Amazon DynamoDB',
            year: 2012,
            developer: 'Amazon',
            significance: 'AWS managed NoSQL',
            features: ['Serverless', 'DAX caching', 'Global tables', 'Streams']
        },
        cosmosdb: {
            name: 'Azure Cosmos DB',
            year: 2017,
            developer: 'Microsoft',
            significance: 'Multi-model global database',
            apis: ['SQL', 'MongoDB', 'Cassandra', 'Gremlin', 'Table']
        },
        ravendb: {
            name: 'RavenDB',
            year: 2010,
            significance: 'ACID document database'
        },
        faunadb: {
            name: 'Fauna',
            year: 2012,
            significance: 'Serverless, strongly consistent'
        }
    },

    // ===========================================================================
    // NOSQL - KEY-VALUE STORES
    // ===========================================================================
    keyValue: {
        redis: {
            name: 'Redis',
            year: 2009,
            developer: 'Salvatore Sanfilippo',
            significance: 'Most popular in-memory data store',
            dataStructures: ['Strings', 'Hashes', 'Lists', 'Sets', 'Sorted Sets', 'Streams', 'HyperLogLog'],
            features: ['Pub/Sub', 'Lua scripting', 'Cluster', 'Sentinel']
        },
        memcached: {
            name: 'Memcached',
            year: 2003,
            developer: 'Brad Fitzpatrick',
            significance: 'Original distributed caching system'
        },
        etcd: {
            name: 'etcd',
            year: 2013,
            developer: 'CoreOS/Red Hat',
            significance: 'Kubernetes config store, Raft consensus'
        },
        consul: {
            name: 'HashiCorp Consul',
            year: 2014,
            significance: 'Service discovery and KV store'
        },
        riak: {
            name: 'Riak',
            year: 2009,
            developer: 'Basho',
            significance: 'Distributed, fault-tolerant'
        },
        leveldb: {
            name: 'LevelDB',
            year: 2011,
            developer: 'Google',
            significance: 'Embedded key-value store, LSM tree'
        },
        rocksdb: {
            name: 'RocksDB',
            year: 2012,
            developer: 'Facebook',
            base: 'LevelDB fork',
            significance: 'High-performance embedded storage'
        },
        foundationdb: {
            name: 'FoundationDB',
            year: 2013,
            developer: 'Apple (acquired)',
            significance: 'ACID distributed KV, Apple iCloud backend'
        },
        tikv: {
            name: 'TiKV',
            year: 2016,
            developer: 'PingCAP',
            significance: 'Distributed transactional KV'
        }
    },

    // ===========================================================================
    // NOSQL - WIDE COLUMN
    // ===========================================================================
    wideColumn: {
        bigtable: {
            name: 'Google Bigtable',
            year: 2005,
            developer: 'Google',
            significance: 'Pioneered wide-column model',
            paper: 'Bigtable: A Distributed Storage System for Structured Data (2006)'
        },
        cassandra: {
            name: 'Apache Cassandra',
            year: 2008,
            developer: 'Facebook (originally)',
            significance: 'High availability, no single point of failure',
            features: ['Tunable consistency', 'Linear scalability', 'CQL']
        },
        hbase: {
            name: 'Apache HBase',
            year: 2008,
            significance: 'Hadoop database, Bigtable clone',
            features: ['HDFS storage', 'Strong consistency']
        },
        scylladb: {
            name: 'ScyllaDB',
            year: 2015,
            significance: 'C++ Cassandra-compatible, 10x faster'
        }
    },

    // ===========================================================================
    // GRAPH DATABASES
    // ===========================================================================
    graph: {
        neo4j: {
            name: 'Neo4j',
            year: 2007,
            developer: 'Neo4j Inc',
            significance: 'Most popular graph database',
            language: 'Cypher query language',
            features: ['Native graph storage', 'ACID transactions']
        },
        amazon_neptune: {
            name: 'Amazon Neptune',
            year: 2018,
            developer: 'Amazon',
            significance: 'AWS managed graph database',
            supports: ['Gremlin', 'SPARQL', 'openCypher']
        },
        arangodb: {
            name: 'ArangoDB',
            year: 2012,
            significance: 'Multi-model (document, graph, key-value)',
            language: 'AQL'
        },
        dgraph: {
            name: 'Dgraph',
            year: 2016,
            significance: 'Distributed graph database',
            language: 'GraphQL+/-'
        },
        tigergraph: {
            name: 'TigerGraph',
            year: 2017,
            significance: 'Enterprise graph analytics'
        },
        janusgraph: {
            name: 'JanusGraph',
            year: 2017,
            significance: 'Scalable graph database (TitanDB fork)'
        }
    },

    // ===========================================================================
    // TIME SERIES DATABASES
    // ===========================================================================
    timeSeries: {
        influxdb: {
            name: 'InfluxDB',
            year: 2013,
            developer: 'InfluxData',
            significance: 'Most popular time series database',
            features: ['InfluxQL', 'Flux', 'Continuous queries']
        },
        prometheus: {
            name: 'Prometheus',
            year: 2012,
            developer: 'SoundCloud',
            significance: 'Monitoring and alerting (CNCF)',
            features: ['PromQL', 'Pull model', 'Alertmanager']
        },
        timescaledb: {
            name: 'TimescaleDB',
            year: 2017,
            significance: 'PostgreSQL extension for time series',
            features: ['Hypertables', 'Continuous aggregates']
        },
        questdb: {
            name: 'QuestDB',
            year: 2019,
            significance: 'High-performance time series',
            features: ['SQL', 'InfluxDB line protocol']
        },
        clickhouse: {
            name: 'ClickHouse',
            year: 2016,
            developer: 'Yandex',
            significance: 'Column-oriented OLAP/time series'
        },
        druid: {
            name: 'Apache Druid',
            year: 2011,
            developer: 'Metamarkets',
            significance: 'Real-time analytics database'
        },
        victoriametrics: {
            name: 'VictoriaMetrics',
            year: 2018,
            significance: 'Prometheus-compatible, efficient storage'
        }
    },

    // ===========================================================================
    // SEARCH ENGINES
    // ===========================================================================
    search: {
        elasticsearch: {
            name: 'Elasticsearch',
            year: 2010,
            developer: 'Elastic NV',
            significance: 'Most popular search engine',
            features: ['Lucene-based', 'REST API', 'Kibana', 'ELK stack']
        },
        solr: {
            name: 'Apache Solr',
            year: 2006,
            significance: 'Enterprise search platform',
            features: ['Lucene-based', 'Faceting', 'SolrCloud']
        },
        opensearch: {
            name: 'OpenSearch',
            year: 2021,
            developer: 'Amazon (Elasticsearch fork)',
            significance: 'Open-source Elasticsearch alternative'
        },
        meilisearch: {
            name: 'Meilisearch',
            year: 2018,
            significance: 'Fast, typo-tolerant search'
        },
        typesense: {
            name: 'Typesense',
            year: 2019,
            significance: 'Open-source Algolia alternative'
        },
        algolia: {
            name: 'Algolia',
            year: 2012,
            significance: 'Hosted search-as-a-service'
        }
    },

    // ===========================================================================
    // VECTOR DATABASES (AI/ML)
    // ===========================================================================
    vector: {
        pinecone: {
            name: 'Pinecone',
            year: 2019,
            significance: 'Managed vector database for ML'
        },
        weaviate: {
            name: 'Weaviate',
            year: 2019,
            significance: 'Open-source vector search'
        },
        milvus: {
            name: 'Milvus',
            year: 2019,
            significance: 'Open-source vector database'
        },
        qdrant: {
            name: 'Qdrant',
            year: 2021,
            significance: 'Vector similarity search engine'
        },
        chroma: {
            name: 'Chroma',
            year: 2022,
            significance: 'AI-native embedding database'
        },
        pgvector: {
            name: 'pgvector',
            year: 2021,
            significance: 'Vector extension for PostgreSQL'
        }
    },

    // ===========================================================================
    // HISTORICAL / LEGACY
    // ===========================================================================
    historical: {
        ims: {
            name: 'IBM IMS',
            year: 1966,
            significance: 'First database system (hierarchical)'
        },
        idms: {
            name: 'IDMS',
            year: 1971,
            significance: 'Network model database (CODASYL)'
        },
        ingres: {
            name: 'Ingres',
            year: 1974,
            developer: 'UC Berkeley',
            significance: 'Influential relational research DB'
        },
        informix: {
            name: 'Informix',
            year: 1980,
            significance: 'Object-relational pioneer (now IBM)'
        },
        sybase: {
            name: 'Sybase',
            year: 1987,
            significance: 'SQL Server ancestor (now SAP)'
        },
        dbase: {
            name: 'dBASE',
            year: 1979,
            significance: 'First microcomputer database'
        },
        foxpro: {
            name: 'FoxPro',
            year: 1984,
            significance: 'Popular xBase database (now MS Visual FoxPro)'
        },
        paradox: {
            name: 'Paradox',
            year: 1985,
            developer: 'Borland',
            significance: 'PC relational database'
        },
        access: {
            name: 'Microsoft Access',
            year: 1992,
            significance: 'Desktop database application'
        },
        filemaker: {
            name: 'FileMaker',
            year: 1985,
            significance: 'Low-code database (Claris/Apple)'
        }
    }
};

// API Endpoints
app.get('/api/databases/categories', (c) => {
    return c.json({ success: true, categories: Object.keys(DATABASE_SYSTEMS) });
});

app.get('/api/databases/search', (c) => {
    const query = (c.req.query('q') || '').toLowerCase();
    const results: any[] = [];

    Object.entries(DATABASE_SYSTEMS).forEach(([category, dbs]) => {
        Object.entries(dbs).forEach(([key, db]: [string, any]) => {
            if (
                (db.name || key).toLowerCase().includes(query) ||
                (db.significance && db.significance.toLowerCase().includes(query))
            ) {
                results.push({ category, key, ...db });
            }
        });
    });

    return c.json({ success: true, resultCount: results.length, results });
});

app.get('/api/databases/category/:category', (c) => {
    const category = c.req.param('category') as keyof typeof DATABASE_SYSTEMS;
    const data = DATABASE_SYSTEMS[category];
    if (!data) return c.json({ error: 'Not found' }, 404);
    return c.json({ success: true, category, databases: data });
});

app.get('/api/databases/relational', (c) => c.json({ success: true, databases: DATABASE_SYSTEMS.relational }));
app.get('/api/databases/nosql', (c) => c.json({ success: true, document: DATABASE_SYSTEMS.document, keyValue: DATABASE_SYSTEMS.keyValue, wideColumn: DATABASE_SYSTEMS.wideColumn }));
app.get('/api/databases/graph', (c) => c.json({ success: true, databases: DATABASE_SYSTEMS.graph }));
app.get('/api/databases/vector', (c) => c.json({ success: true, databases: DATABASE_SYSTEMS.vector }));

app.get('/health', (c) => c.json({ status: 'healthy', worker: 'database-systems-worker' }));

export default app;
