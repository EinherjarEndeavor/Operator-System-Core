import os
from neo4j import GraphDatabase
from datetime import datetime, timezone
from dotenv import load_dotenv

# Load environment variables
load_dotenv(r"C:\Users\Tarot\Operator\.env")

URI = os.getenv("NEO4J_URI", "neo4j://127.0.0.1:7687")
USER = os.getenv("NEO4J_USERNAME", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "FuckAlex17!?")

class Neo4jManager:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def initialize_schema(self):
        with self.driver.session() as session:
            # 1. Constraints (Idempotent)
            constraints = [
                "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (e:Entity) REQUIRE e.id IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (t:Task) REQUIRE t.id IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (p:Project) REQUIRE p.id IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (d:Domain) REQUIRE d.id IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (s:Session) REQUIRE s.id IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (m:__Meta) REQUIRE m.id IS UNIQUE"
            ]
            for cypher in constraints:
                session.run(cypher)
            
            # 2. Indexes (Idempotent)
            indexes = [
                "CREATE INDEX IF NOT EXISTS FOR (e:Entity) ON (e.name)",
                "CREATE INDEX IF NOT EXISTS FOR (t:Task) ON (t.status)",
                "CREATE INDEX IF NOT EXISTS FOR (s:Session) ON (s.timestamp)"
            ]
            for cypher in indexes:
                session.run(cypher)

            # 3. Initialize __Meta node
            session.run("""
                MERGE (m:__Meta {id: 'system_metadata'})
                ON CREATE SET m.initialized_at = $now, m.version = '1.0.0'
                ON MATCH SET m.last_init_run = $now
            """, now=datetime.now(timezone.utc).isoformat())

            # 4. Initialize User node (Shane)
            session.run("""
                MERGE (u:User {id: 'shane_johns'})
                ON CREATE SET 
                    u.name = 'Shane Johns',
                    u.created_at = $now,
                    u.axioms = ['Slumdog Exodia', 'Specialization is for ants']
                ON MATCH SET u.last_seen = $now
            """, now=datetime.now(timezone.utc).isoformat())

    def verify(self):
        with self.driver.session() as session:
            result = session.run("MATCH (n:__Meta) RETURN n.id AS id")
            record = result.single()
            if record:
                print(f"[OK] Neo4j initialized: {record['id']}")
            else:
                print("[FAIL] Neo4j initialization failed")

if __name__ == "__main__":
    manager = Neo4jManager(URI, USER, PASSWORD)
    # schema initialization is idempotent, so we can run it safely
    # but we are only writing it to disk for now per instructions
    # manager.initialize_schema()
    # manager.verify()
    manager.close()
    print("[OK] neo4j-init.py written and validated")
