resource "aws_iam_role" "wasp_readonly" {
  name = "wasp-readonly-role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"Service": "ec2.amazonaws.com"},
    "Action": "sts:AssumeRole"
  }]
}
EOF
}

resource "aws_iam_role_policy" "wasp_readonly_policy" {
  role = aws_iam_role.wasp_readonly.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = [
        "s3:GetObject",
        "s3:ListBucket",
        "logs:DescribeLogGroups",
        "logs:GetLogEvents"
      ],
      Effect = "Allow",
      Resource = "*"
    }]
  })
}
