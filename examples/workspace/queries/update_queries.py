import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import sql

w = WorkspaceClient()

query = w.queries.create(
    query=sql.CreateQueryRequestQuery(
        display_name=f"sdk-{time.time_ns()}",
        description="This is a test query created from the SDK",
        query_text="SELECT 1",
    )
)

w.queries.update(
    id=query.id,
    query=sql.UpdateQueryRequestQuery(
        description="This is a test query updated from the SDK",
        query_text="SELECT 2",
    ),
    update_mask="description,query_text",
)

# cleanup
w.queries.delete(id=query.id)
