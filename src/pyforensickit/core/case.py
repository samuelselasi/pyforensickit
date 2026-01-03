from datetime import datetime
import uuid

class ForensicCase:
    def __init__(
        self,
        case_id=None,
        investigator=None,
        description=None
    ):
        self.case_id = case_id or self._generate_case_id()
        self.investigator = investigator
        self.description = description
        self.analysis_started = datetime.utcnow().isoformat() + "Z"

    def to_dict(self):
        return {
            "case_id": self.case_id,
            "investigator": self.investigator,
            "description": self.description,
            "analysis_started_utc": self.analysis_started,
            "tool": {
                "name": "PyForensicKit",
                "version": "0.1.0",
                "platform": "linux"
            }
        }

    def _generate_case_id(self):
        return f"PFK-{uuid.uuid4()}"
